project(dxtbx)

add_library( dxtbx INTERFACE )
target_include_directories(dxtbx INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_subdirectory(boost_python)
add_subdirectory(format)
add_subdirectory(model)
