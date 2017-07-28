add_executable(cbflib.tst_memory tst_memory.cpp)
target_link_libraries(cbflib.tst_memory cbf)
add_test(NAME cbflib.tst_memory COMMAND cbflib.tst_memory)

add_subdirectory(boost_python)
