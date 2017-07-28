add_python_library ( dials_algorithms_spot_finding_ext
            spot_finding_ext.cc )
target_link_libraries(dials_algorithms_spot_finding_ext cctbx scitbx_boost_python)

