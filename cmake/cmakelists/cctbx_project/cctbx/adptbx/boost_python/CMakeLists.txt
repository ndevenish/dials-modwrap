add_python_library ( cctbx_adptbx_ext
            adptbx_ext.cpp
            hirshfeld.cpp )
target_link_libraries(cctbx_adptbx_ext cctbx scitbx_boost_python)

