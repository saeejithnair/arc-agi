#%%
import arckit
import arckit.vis as vis
#%%
train_set, eval_set = arckit.load_data() # Load ARC1 train/eval
print(train_set)
print(train_set[0])
task = arckit.load_single('007bbfb7')
print(task)
#%%
grid = vis.draw_grid(task.train[0][0], xmax=3, ymax=3, padding=.5, label='Example')
vis.output_drawing(grid, "images/arcshow_example.png")

# %%
task = vis.draw_task(train_set[0], width=10, height=6, label='Example')
vis.output_drawing(grid, "images/arcshow_example.png") # svg/pdf/png
# %%
