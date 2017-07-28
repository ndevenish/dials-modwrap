add_python_library ( cctbx_translation_search_ext
            fast_nv1995.cpp
            fast_terms.cpp
            symmetry_flags.cpp
            translation_search_ext.cpp )
target_link_libraries(cctbx_translation_search_ext cctbx omptbx scitbx_boost_python)

