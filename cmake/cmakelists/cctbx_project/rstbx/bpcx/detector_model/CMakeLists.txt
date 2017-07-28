add_python_library ( rstbx_bpcx_detector_model_ext
            detector_model_ext.cpp
            sensor.cpp )
target_link_libraries(rstbx_bpcx_detector_model_ext cctbx rstbx scitbx_boost_python)

