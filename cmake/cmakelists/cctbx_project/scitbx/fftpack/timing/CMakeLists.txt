add_executable(fftpack_timer fftpack_timer.cpp)
target_link_libraries(fftpack_timer omptbx)

add_executable(test0 test0.cpp)
target_link_libraries(test0 omptbx)
add_test(NAME test0 COMMAND test0)

