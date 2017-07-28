add_python_library ( rstbx_diffraction_fastbragg_ext
            fastbragg_ext.cpp
            fastbragg.cpp )
target_link_libraries(rstbx_diffraction_fastbragg_ext cctbx rstbx scitbx_boost_python)

