module fortran

  Implicit None
  Private

  integer, parameter :: r8 = selected_real_kind(15, 307)

  public :: print_array

contains

  subroutine print_array(x)

    real(kind=r8), dimension(10), intent(in) :: x

    integer :: i

    do i = 1, 10
      print*, x(i)
    end do

  end subroutine print_array

end module fortran
