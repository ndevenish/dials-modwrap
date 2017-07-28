project(chiltbx)

add_library( chiltbx INTERFACE )
target_include_directories(chiltbx INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_executable(handle_test handle_test.cpp)
add_test(NAME handle_test COMMAND handle_test)

