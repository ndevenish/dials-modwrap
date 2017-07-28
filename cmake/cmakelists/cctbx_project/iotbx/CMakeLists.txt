project(iotbx)

add_library( iotbx INTERFACE )
target_include_directories(iotbx INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_libtbx_refresh_command( ${CMAKE_CURRENT_SOURCE_DIR}/libtbx_refresh.py
     OUTPUT ${CMAKE_BINARY_DIR}/iotbx/pdb/hybrid_36_fem.cpp )

add_python_library ( iotbx_wildcard_ext
            wildcard_ext.cpp )

add_subdirectory(ccp4_map)
add_subdirectory(detectors)
add_subdirectory(dsn6)
add_subdirectory(misc)
add_subdirectory(mtz)
add_subdirectory(pdb)
add_subdirectory(shelx)
add_subdirectory(xplor)
