add_python_library ( dials_algorithms_profile_model_modeller_ext
            ext.cc
            modeller.cc
            sampler.cc )
target_link_libraries(dials_algorithms_profile_model_modeller_ext cctbx scitbx_boost_python)

