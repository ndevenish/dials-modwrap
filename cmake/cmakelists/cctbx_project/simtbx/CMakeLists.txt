project(simtbx)

add_library( simtbx INTERFACE )
target_include_directories(simtbx INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_subdirectory(nanoBragg)
