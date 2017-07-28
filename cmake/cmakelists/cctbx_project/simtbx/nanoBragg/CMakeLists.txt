add_python_library ( simtbx_nanoBragg_ext
            nanoBragg_ext.cpp
            nanoBragg.cpp )
target_link_libraries(simtbx_nanoBragg_ext cctbx scitbx_boost_python)

