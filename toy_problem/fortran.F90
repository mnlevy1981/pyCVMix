module fortran

  Implicit None
  Private

  public :: print_hello

contains

  subroutine print_hello()

    print*, "Hello world (module edition)!"

  end subroutine print_hello

end module fortran
