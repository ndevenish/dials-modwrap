add_python_library ( scitbx_stl_map_ext
            map_ext.cpp )
target_link_libraries(scitbx_stl_map_ext scitbx_boost_python)

add_python_library ( scitbx_stl_set_ext
            set_ext.cpp )
target_link_libraries(scitbx_stl_set_ext scitbx_boost_python)

add_python_library ( scitbx_stl_vector_ext
            vector_ext.cpp )
target_link_libraries(scitbx_stl_vector_ext scitbx_boost_python)

