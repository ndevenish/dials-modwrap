add_python_library ( cctbx_emma_ext
            emma_ext.cpp )
target_link_libraries(cctbx_emma_ext cctbx scitbx_boost_python)

add_python_library ( cctbx_french_wilson_ext
            french_wilson_ext.cpp )
target_link_libraries(cctbx_french_wilson_ext cctbx scitbx_boost_python)

add_python_library ( cctbx_orientation_ext
            orientation_ext.cpp )
target_link_libraries(cctbx_orientation_ext cctbx scitbx_boost_python)

add_python_library ( cctbx_statistics_ext
            statistics_ext.cpp )
target_link_libraries(cctbx_statistics_ext cctbx scitbx_boost_python)

