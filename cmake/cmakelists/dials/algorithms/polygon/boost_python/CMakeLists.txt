add_python_library ( dials_algorithms_polygon_ext
            polygon_ext.cc )
target_link_libraries(dials_algorithms_polygon_ext cctbx scitbx_boost_python)

add_python_library ( dials_algorithms_polygon_spatial_interpolation_ext
            spatial_interpolation_ext.cc )
target_link_libraries(dials_algorithms_polygon_spatial_interpolation_ext cctbx scitbx_boost_python)

