module fortran

  Implicit None
  Private

  integer, parameter :: r8 = selected_real_kind(15, 307)

  public :: print_array

contains

  subroutine print_array(x)

    real(kind=r8), dimension(2,5), intent(in) :: x

    integer :: j

    do j = 1,5
      print*, x(:,j)
    end do

  end subroutine print_array

end module fortran
