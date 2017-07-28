add_python_library ( dials_algorithms_shoebox_ext
            find_overlapping.cc
            mask_builder.cc
            mask_code.cc
            mask_empirical.cc
            mask_overlapping.cc
            overload_checker.cc
            shoebox_ext.cc )
target_link_libraries(dials_algorithms_shoebox_ext cctbx ann scitbx_boost_python)

