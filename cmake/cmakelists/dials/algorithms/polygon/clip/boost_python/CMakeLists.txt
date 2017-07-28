add_python_library ( dials_algorithms_polygon_clip_ext
            clip_ext.cc )
target_link_libraries(dials_algorithms_polygon_clip_ext cctbx scitbx_boost_python)

