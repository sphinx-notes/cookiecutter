# Create a demo from the current template.
# NOTE: only committed changes take effect.
.PHONY: demo
demo:
	rm -rf demo/
	cruft create .
