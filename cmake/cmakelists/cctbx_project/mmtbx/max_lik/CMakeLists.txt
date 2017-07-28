add_python_library ( mmtbx_max_lik_ext
            max_lik_ext.cpp
            max_lik.cpp )
target_link_libraries(mmtbx_max_lik_ext cctbx scitbx_boost_python)

