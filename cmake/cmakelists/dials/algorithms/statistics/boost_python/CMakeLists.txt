add_python_library ( dials_algorithms_statistics_ext
            statistics_ext.cc )
target_link_libraries(dials_algorithms_statistics_ext cctbx scitbx_boost_python)

