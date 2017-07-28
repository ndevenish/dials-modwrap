project(cbflib_adaptbx)

add_library( cbflib_adaptbx INTERFACE )
target_include_directories(cbflib_adaptbx INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_libtbx_refresh_command( ${CMAKE_CURRENT_SOURCE_DIR}/libtbx_refresh.py
     OUTPUT ${CMAKE_BINARY_DIR}/lib/pycbf.py )

add_subdirectory(detectors)
