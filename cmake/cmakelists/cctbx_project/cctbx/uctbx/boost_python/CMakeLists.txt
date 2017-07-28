add_python_library ( cctbx_uctbx_ext
            fast_minimum_reduction.cpp
            uctbx_ext.cpp )
target_link_libraries(cctbx_uctbx_ext cctbx scitbx_boost_python)

