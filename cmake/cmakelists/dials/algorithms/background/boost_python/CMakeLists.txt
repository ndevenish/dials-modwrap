add_python_library ( dials_algorithms_background_ext
            background_ext.cc
            helpers.cc )
target_link_libraries(dials_algorithms_background_ext cctbx scitbx_boost_python)

add_python_library ( dials_algorithms_background_modeller_ext
            modeller_ext.cc )
target_link_libraries(dials_algorithms_background_modeller_ext cctbx scitbx_boost_python)

