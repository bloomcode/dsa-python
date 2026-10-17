PY ?= python3

.PHONY: test progress

# make test            every exercise
# make test EX=13.2    one exercise
# make test EX=13      one chapter
test:
ifeq ($(EX),)
	$(PY) -m pytest -q
else
	@ch=$$(printf '%02d' $$(echo "$(EX)" | cut -d. -f1)); f=$$(ls tests/test_ch$${ch}_*.py); \
	case "$(EX)" in \
	  *.*) $(PY) -m pytest -q "$$f::test_ex_$$(echo "$(EX)" | tr . _)" ;; \
	  *) $(PY) -m pytest -q "$$f" ;; \
	esac
endif

progress:
	$(PY) tools/progress.py
