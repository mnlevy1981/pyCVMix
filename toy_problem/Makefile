SRC_FILES=fortran.F90 fortran_nomod.F90

.PHONY: all
all: libfort.so

.PHONY: clean
clean:
	rm -f libfort.so fortran.mod

libfort.so: $(SRC_FILES)
	gfortran -shared -o $@ -fPIC $(SRC_FILES)
