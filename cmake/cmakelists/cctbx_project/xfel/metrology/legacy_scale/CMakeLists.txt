add_library ( legacy_scale 
            scale_core.cpp
            bandpass_gaussian.cpp )
target_link_libraries(legacy_scale annlib annlib_adaptbx xfel)

add_python_library ( xfel_legacy_scale_ext
            ext.cpp )
target_link_libraries(xfel_legacy_scale_ext cctbx legacy_scale ann scitbx_boost_python)

