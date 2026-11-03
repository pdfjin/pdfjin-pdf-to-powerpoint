import io, tempfile, os
from pathlib import Path
from typing import Union
from pdf2image import convert_from_path, convert_from_bytes
from pptx import Presentation


def pdf_to_powerpoint(input_pdf: Union[str, Path, bytes], output_pptx: Union[str, Path]) -> Path:
    prs = Presentation()
    if isinstance(input_pdf, (str, Path)):
        images = convert_from_path(str(input_pdf))
    else:
        images = convert_from_bytes(input_pdf)

    for img in images:
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
            img.save(tmp.name, format="JPEG")
            slide = prs.slides.add_slide(prs.slide_layouts[6])
            slide.shapes.add_picture(tmp.name, 0, 0, width=prs.slide_width, height=prs.slide_height)
            os.unlink(tmp.name)

    out_p = Path(output_pptx)
    out_p.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(out_p))
    return out_p
