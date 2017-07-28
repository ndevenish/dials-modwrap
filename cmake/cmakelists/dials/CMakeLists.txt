project(dials)

add_library( dials INTERFACE )
target_include_directories(dials INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_subdirectory(algorithms)
add_subdirectory(array_family)
add_subdirectory(model)
add_subdirectory(test)
add_subdirectory(util)
add_subdirectory(viewer)
