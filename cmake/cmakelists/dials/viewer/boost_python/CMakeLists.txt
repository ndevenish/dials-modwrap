add_python_library ( dials_viewer_ext
            RGB_2d.cc
            RGB_2d_ext.cc )
target_link_libraries(dials_viewer_ext cctbx scitbx_boost_python)

