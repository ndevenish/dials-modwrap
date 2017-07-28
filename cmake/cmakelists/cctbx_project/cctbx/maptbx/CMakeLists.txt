add_library ( asymmetric_map 
            asymmetric_map.cpp )
target_link_libraries(asymmetric_map cctbx cctbx_sgtbx_asu iotbx_xplor omptbx)

add_python_library ( cctbx_asymmetric_map_ext
            asymmetric_map_ext.cpp )
target_link_libraries(cctbx_asymmetric_map_ext cctbx_sgtbx_asu iotbx_xplor asymmetric_map cctbx omptbx scitbx_boost_python)

add_subdirectory(boost_python)
