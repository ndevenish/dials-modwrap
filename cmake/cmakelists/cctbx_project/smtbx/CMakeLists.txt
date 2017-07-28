project(smtbx)

add_library( smtbx INTERFACE )
target_include_directories(smtbx INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_libtbx_refresh_command( ${CMAKE_CURRENT_SOURCE_DIR}/libtbx_refresh.py
     OUTPUT ${CMAKE_BINARY_DIR}/include/smtbx/boost_python/flex_fwd.h )

add_subdirectory(ab_initio)
add_subdirectory(array_family)
add_subdirectory(refinement)
add_subdirectory(stl)
add_subdirectory(structure_factors)
