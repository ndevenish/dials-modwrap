add_python_library ( mmtbx_geometry_asa_ext
            asa_ext.cpp )
target_link_libraries(mmtbx_geometry_asa_ext scitbx_boost_python)

add_python_library ( mmtbx_geometry_clash_ext
            clash_ext.cpp )
target_link_libraries(mmtbx_geometry_clash_ext scitbx_boost_python)

add_python_library ( mmtbx_geometry_indexing_ext
            indexing_ext.cpp )
target_link_libraries(mmtbx_geometry_indexing_ext scitbx_boost_python)

add_python_library ( mmtbx_geometry_primitive_ext
            primitive_ext.cpp )
target_link_libraries(mmtbx_geometry_primitive_ext scitbx_boost_python)

add_python_library ( mmtbx_geometry_shared_types_ext
            shared_types_ext.cpp )
target_link_libraries(mmtbx_geometry_shared_types_ext scitbx_boost_python)

add_python_library ( mmtbx_geometry_sphere_surface_sampling_ext
            sphere_surface_sampling_ext.cpp )
target_link_libraries(mmtbx_geometry_sphere_surface_sampling_ext scitbx_boost_python)

