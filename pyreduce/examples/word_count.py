from ..api import mrpipeline

def main():
    # Create a new pipeline
    pipeline = mrpipeline.Pipeline()
    pipeline.execute()

if __name__ == "__main__":
    main()