add_library ( xfel_mono_sim 
            bandpass_gaussian.cpp
            ccixfel_core.cpp )
target_link_libraries(xfel_mono_sim annlib annlib_adaptbx xfel)

add_python_library ( xfel_mono_sim_ext
            ext.cpp )
target_link_libraries(xfel_mono_sim_ext cctbx ann xfel_mono_sim scitbx_boost_python)

