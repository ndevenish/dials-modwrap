add_python_library ( mmtbx_rotamer_fit_ext
            fit_ext.cpp )
target_link_libraries(mmtbx_rotamer_fit_ext cctbx scitbx_boost_python)

