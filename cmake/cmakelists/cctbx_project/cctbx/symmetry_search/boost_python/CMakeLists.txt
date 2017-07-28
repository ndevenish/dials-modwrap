add_python_library ( cctbx_symmetry_search_ext
            symmetry_search_ext.cpp )
target_link_libraries(cctbx_symmetry_search_ext cctbx omptbx scitbx_boost_python)

