add_python_library ( dials_algorithms_integration_sum_ext
            integration_sum_ext.cc
            summation.cc )
target_link_libraries(dials_algorithms_integration_sum_ext cctbx scitbx_boost_python)

