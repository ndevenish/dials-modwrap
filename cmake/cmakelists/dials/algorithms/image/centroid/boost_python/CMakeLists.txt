add_python_library ( dials_algorithms_image_centroid_ext
            centroid_ext.cc )
target_link_libraries(dials_algorithms_image_centroid_ext cctbx scitbx_boost_python)

