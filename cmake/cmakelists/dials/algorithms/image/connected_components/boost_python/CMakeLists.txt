add_python_library ( dials_algorithms_image_connected_components_ext
            connected_components_ext.cc )
target_link_libraries(dials_algorithms_image_connected_components_ext cctbx scitbx_boost_python)

