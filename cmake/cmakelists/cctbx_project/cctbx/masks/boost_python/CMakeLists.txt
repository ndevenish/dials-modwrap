add_python_library ( cctbx_masks_ext
            masks_ext.cpp )
target_link_libraries(cctbx_masks_ext cctbx omptbx scitbx_boost_python)

