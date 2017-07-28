add_python_library ( cctbx_array_family_flex_ext
            flex_ext.cpp
            flex_hendrickson_lattman.cpp
            flex_miller_index.cpp
            flex_xray_scatterer.cpp )
target_link_libraries(cctbx_array_family_flex_ext cctbx scitbx_boost_python)

