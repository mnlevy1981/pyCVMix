module fortran

  Implicit None
  Private

  integer, parameter :: r8 = selected_real_kind(15, 307)

  type :: my_type
    real(r8) :: one_val
    real(r8), dimension(2) :: two_vals
    real(r8), dimension(:), allocatable :: n_vals
  end type my_type

  public :: print_type
  public :: my_type

contains

  subroutine print_type(x)

    type(my_type), intent(in) :: x

    print*, x%one_val
    print*, x%two_vals
    if (allocated(x%n_vals)) print*, x%n_vals

  end subroutine print_type

end module fortran
