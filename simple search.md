simple search

- main.py

  - 直接运行即可
  - 用signal让每一个data最多运行1s，但是300*300的貌似一个也跑不出来，小一点的还没有试

- gamut.jar

  - 生成数据的包，改了一点格式，可能要版本高一点的jdk才能运行？
  - 通过`prepare_data.py`来调用它，官方文档在 http://gamut.stanford.edu/

- prepare_data.py

  - 在当前文件夹下生成数据，可以调整矩阵大小和游戏类型，具体见官方文档

- utils.lp.py

  - `import pulp`
  - `model.status == -1`表示无解，否则找到解，assert的语句是在验证解的合法性（但可能有精度问题，如果要用建议适当调大epsilon）

  

  

  

  