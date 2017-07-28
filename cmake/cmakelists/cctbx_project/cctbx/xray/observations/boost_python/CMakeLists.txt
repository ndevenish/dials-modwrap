add_python_library ( cctbx_xray_observations_ext
            observations.cpp
            observations_ext.cpp )
target_link_libraries(cctbx_xray_observations_ext cctbx scitbx_boost_python)

