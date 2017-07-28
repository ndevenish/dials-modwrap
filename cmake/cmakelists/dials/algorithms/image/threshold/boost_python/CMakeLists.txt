add_python_library ( dials_algorithms_image_threshold_ext
            local.cc
            threshold_ext.cc
            unimodal.cc )
target_link_libraries(dials_algorithms_image_threshold_ext cctbx scitbx_boost_python)

