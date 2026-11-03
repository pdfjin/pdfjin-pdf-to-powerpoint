import sys, argparse
try:
    from .core import pdf_to_powerpoint
    from . import __version__
except (ImportError, ValueError):
    from pdfjin_pdf_to_powerpoint.core import pdf_to_powerpoint
    from pdfjin_pdf_to_powerpoint import __version__


def main():
    p = argparse.ArgumentParser(prog="pdfjin-pdf-to-powerpoint", description="Convert PDF to PowerPoint.")
    p.add_argument("input", help="Input PDF file")
    p.add_argument("-o", "--output", required=True, help="Output PPTX file")
    p.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    args = p.parse_args()
    try:
        pdf_to_powerpoint(args.input, args.output)
        print(f"PowerPoint saved -> {args.output}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr); sys.exit(1)


if __name__ == "__main__":
    main()
