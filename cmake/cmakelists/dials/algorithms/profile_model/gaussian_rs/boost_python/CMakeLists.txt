add_python_library ( dials_algorithms_profile_model_gaussian_rs_ext
            gaussian_rs_ext.cc )
target_link_libraries(dials_algorithms_profile_model_gaussian_rs_ext cctbx scitbx_boost_python)

