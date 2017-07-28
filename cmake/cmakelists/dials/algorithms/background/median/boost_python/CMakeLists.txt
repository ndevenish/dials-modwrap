add_python_library ( dials_algorithms_background_median_ext
            ext.cc )
target_link_libraries(dials_algorithms_background_median_ext cctbx scitbx_boost_python)

